import librosa
import librosa.display
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

def display(mel_spectrogram):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(mel_spectrogram,
                            x_axis='time',
                            y_axis='mel',
                            sr=sampling_rate)
    plt.show()
    

audio_path = '../ffmpeg/vocal-noise-rem-only.aac'
scale, sampling_rate = librosa.load(audio_path)

mel_spectrogram = librosa.feature.melspectrogram(y=scale, sr=sampling_rate, n_fft=2048, hop_length=512, n_mels=10)

log_mel_spectogram = librosa.power_to_db(mel_spectrogram)

interval_length = 10
total_duration = len(scale) / sampling_rate
num_intervals = int(total_duration // interval_length)

mel_spectrograms = list()
for interval in range(num_intervals):
    # Define the start and end index for the current interval
    start_index = interval * interval_length * sampling_rate
    end_index = (interval + 1) * interval_length * sampling_rate

    # Get the audio slice for the current interval
    interval_audio = scale[start_index:end_index]

    # Obtain the Mel spectrogram for the interval
    interval_mel_spec = librosa.feature.melspectrogram(y=interval_audio, sr=sampling_rate, n_fft=2048, hop_length=512, n_mels=10)

    interval_log_mel_spec = librosa.power_to_db(interval_mel_spec)

    # Append the Mel spectrogram to the list
    mel_spectrograms.append(interval_log_mel_spec)

df = pd.read_csv('../prediction.csv')

actual_values = df['Output Category']

# Convert to numpy arrays and add a channel dimension
mel_spectrograms = np.array(mel_spectrograms)
mel_spectrograms = mel_spectrograms[..., np.newaxis]  # Add channel dimension

mel_train, mel_test,  actual_train, actual_test = train_test_split(mel_spectrograms, actual_values,
                                                                    random_state=104,  
                                                                    test_size=0.25,  
                                                                    shuffle=False)

# Input shape
# input_shape = (mel_spectrograms.shape[1], mel_spectrograms.shape[2], 1)
# input_shape
input_shape = mel_spectrograms[0].shape

num_classes = 2
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(mel_train, actual_train, epochs=10)

model.evaluate(mel_test, actual_test)

prediction = model.predict(mel_spectrograms)
prediction

predicted_values = np.argmax(prediction, axis=1)
# predicted_values
# predicted_values.round()
# predicted_values = predicted_values.astype(int)
# predicted_values

actual_values_np = actual_values.to_numpy()
# actual_values_np

np.sum(predicted_values == actual_values_np)

df['Finalprediction'] = predicted_values

print(df.head(50))

df.to_csv('../prediction.csv')

audio_path = '../serve-vocal-noise-rem-only.aac'
scale, sampling_rate = librosa.load(audio_path)

mel_spectrograms = list()
for interval in range(num_intervals):
    # Define the start and end index for the current interval
    start_index = interval * interval_length * sampling_rate
    end_index = (interval + 1) * interval_length * sampling_rate

    # Get the audio slice for the current interval
    interval_audio = scale[start_index:end_index]

    # Obtain the Mel spectrogram for the interval
    interval_mel_spec = librosa.feature.melspectrogram(y=interval_audio, sr=sampling_rate, n_fft=2048, hop_length=512, n_mels=10)

    interval_log_mel_spec = librosa.power_to_db(interval_mel_spec)

    # Append the Mel spectrogram to the list
    mel_spectrograms.append(interval_log_mel_spec)

predictions = model.predict(mel_spectrograms)

predicted_values = np.argmax(prediction, axis=1)

df_serving = pd.DataFrame()

