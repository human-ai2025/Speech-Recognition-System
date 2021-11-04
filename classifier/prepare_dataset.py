# Extract the audio feature from the files and save it in json file.
# MFCC-> Mel-frequency cepstral coefficients. [time stamps, number of coefficients]

import librosa
import os
import json

DATASET_PATH = "C:\\Users\\tarini.m\\Desktop\\audio-app\\dataset"
JSON_PATH = "data.json"
SAMPLES_TO_CONSIDER = 22050  # 1 sec of audio
COUNT = 1000


# we save the pre-processing before the training cause its time consuming
def prepare_dataset(dataset_path: str, json_path: str, COUNT: int, num_mfcc: int = 13, hop_length: int = 512, n_fft: int = 2048) -> None:
    """Extracts MFCCs from music dataset and saves them into a json file.
        :param dataset_path: Path to dataset
        :param json_path: Path to json file used to save MFCCs
        :param num_mfcc: Number of coefficients to extract
        :param n_fft: Interval we consider to apply FFT. Measured in # of samples
        :param hop_length: Sliding window for FFT. Measured in # of samples
        :return:
        """

    # dictionary where we'll store mapping, labels, MFCCs and file names
    data = {
        "mapping": [],                  # will store the word mapping
        "labels": [],                   # will store the labels
        "MFCCs": [],                    # will store the mfcc
        "files": []                     # will store the path
    }

    # loop through all sub-dirs
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

        # ensure we're at sub-folder level
        if dirpath is not dataset_path:

            # save label (i.e., sub-folder name) in the mapping
            print(dirpath)
            label = dirpath.split("\\")[-1]
            print(label)
            data["mapping"].append(label)
            print("\nProcessing: '{}'".format(label))

            count = 0
            # process all audio files in sub-dir and store MFCCs
            for f in filenames:
                count += 1
                if count < COUNT:
                    file_path = os.path.join(dirpath, f)

                    # load audio file and slice it to ensure length consistency among different files
                    signal, sample_rate = librosa.load(file_path)

                    # drop audio files with less than pre-decided number of samples
                    if len(signal) >= SAMPLES_TO_CONSIDER:
                        # ensure consistency of the length of the signal
                        signal = signal[:SAMPLES_TO_CONSIDER]

                        # extract MFCCs
                        MFCCs = librosa.feature.mfcc(signal, sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
                                                     hop_length=hop_length)

                        # store data for analysed track
                        data["MFCCs"].append(MFCCs.T.tolist())
                        data["labels"].append(i - 1)
                        data["files"].append(file_path)
                        print("{}: {}".format(file_path, i - 1))

    # save data in json file
    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)


if __name__ == "__main__":
    prepare_dataset(DATASET_PATH, JSON_PATH, COUNT)

