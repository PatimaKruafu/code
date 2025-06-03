import librosa
import sys

def extract_beat_timestamps(audio_file_path, output_file_path):
    """
    Extracts beat timestamps from an audio file and saves them to a text file.

    Args:
        audio_file_path (str): Path to the input audio file (e.g., .wav, .mp3).
        output_file_path (str): Path to save the output timestamps (e.g., beats.txt).
    """
    try:
        print(f"Loading audio file: {audio_file_path}")
        # Load the audio file
        # sr=None means load with original sample rate
        # For MASH, often a lower sample rate for analysis is fine if needed for speed
        y, sr = librosa.load(audio_file_path, sr=None)
        print(f"Audio loaded. Sample rate: {sr} Hz, Duration: {len(y)/sr:.2f} seconds")

        # Estimate beat times
        # tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        # For more direct timestamps:
        beat_times = librosa.onset.onset_detect(y=y, sr=sr, units='time', backtrack=False)
        
        # An alternative using tempo and beat frames directly from beat_track
        # tempo, beat_frames_indices = librosa.beat.beat_track(y=y, sr=sr)
        # beat_times = librosa.frames_to_time(beat_frames_indices, sr=sr)

        print(f"Estimated {len(beat_times)} beats.")
        # print(f"Estimated tempo: {tempo:.2f} bpm")

        with open(output_file_path, 'w') as f:
            for t_sec in beat_times:
                f.write(f"{t_sec:.4f}\n") # Write timestamp in seconds, 4 decimal places

        print(f"Beat timestamps saved to: {output_file_path}")
        print("Timestamps (first 10):")
        for i, t in enumerate(beat_times[:10]):
            print(f"  {t:.4f}")

    except Exception as e:
        print(f"Error processing audio: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_beats.py <path_to_audio_file> <path_to_output_txt>")
        sys.exit(1)

    audio_path = sys.argv[1]
    output_path = sys.argv[2]
    extract_beat_timestamps(audio_path, output_path)