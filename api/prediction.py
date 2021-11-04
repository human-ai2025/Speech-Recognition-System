import tensorflow.keras as tf
import librosa
import numpy as np

samples_to_consider = 22050
model_dir = "model_weights/model_trial1.h5"

class _Keyword_Spotting_Service:
    """
    Singleton class for keyword spotting inference with trained models.
    :param model: Trained model
    """
    model = None
    mappings = [
        "bed",
        "bird",
        "cat",
        "dog",
        "down",
        "eight",
        "five",
        "four",
        "go",
        "happy",
        "house",
        "left",
        "marvin",
        "nine",
        "no",
        "off",
        "on",
        "one",
        "right",
        "seven",
        "sheila",
        "six",
        "stop",
        "three",
        "tree",
        "two",
        "up",
        "wow",
        "yes",
        "zero",
        "_background_noise_"
    ]

    _instance = None


    def preprocess(self, file_path, num_mfcc=13, n_fft=2048, hop_length=512):
        """Extract MFCCs from audio file.
        :param file_path (str): Path of audio file
        :param num_mfcc (int): # of coefficients to extract
        :param n_fft (int): Interval we consider to apply STFT. Measured in # of samples
        :param hop_length (int): Sliding window for STFT. Measured in # of samples
        :return MFCCs (ndarray): 2-dim array with MFCC data of shape (# time steps, # coefficients)
        """

        # load audio file
        signal, sample_rate = librosa.load(file_path)

        if len(signal) >= samples_to_consider:
            # ensure consistency of the length of the signal
            signal = signal[:samples_to_consider]

            # extract MFCCs
            MFCCs = librosa.feature.mfcc(signal, sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
                                         hop_length=hop_length)
        return MFCCs.T

    def predict(self, file_path: str):
        """
        :param file_path: The file path  to predict
        :return:
        """
        # extract the MFCC
        mfccs = self.preprocess(file_path)  # (#segments, #coefficients)
        # convert the mfcc array into 4d array -> (#samples, #segments, #coefficients, #channels)
        mfccs = mfccs[np.newaxis, ..., np.newaxis]

        # make prediction
        predictions = self.model.predict(mfccs)
        predicted_index = np.argmax(predictions)
        predicted_keyword = self.mappings[predicted_index]

        return predicted_keyword, predicted_index


def Keyword_Spotting_Service():
    """Factory function for Keyword_Spotting_Service class. Singleton
    :return _Keyword_Spotting_Service._instance (_Keyword_Spotting_Service):
    """
    # ensure an instance is created only the first time the factory function is called
    if _Keyword_Spotting_Service._instance is None:
        _Keyword_Spotting_Service._instance = _Keyword_Spotting_Service()
        _Keyword_Spotting_Service.model = tf.models.load_model(model_dir)
    return _Keyword_Spotting_Service._instance