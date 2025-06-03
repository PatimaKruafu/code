import librosa
import sys

def detect_beats(audio_file_path, output_file_path):
    try:
        # Load the audio file
        print(f"Loading audio file: {audio_file_path}")
        y, sr = librosa.load(audio_file_path)

        # Estimate tempo and detect beats
        print("Estimating tempo and detecting beats...")
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        
        # Convert beat frames to timestamps in seconds
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)

        print(f"Estimated tempo: {tempo:.2f} beats per minute")
        print(f"Found {len(beat_times)} beats.")

        # Save timestamps to the output file
        with open(output_file_path, 'w') as f:
            for t in beat_times:
                f.write(f"{t:.4f}\n") # Write each timestamp on a new line, 4 decimal places
        
        print(f"Beat timestamps saved to: {output_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python beat_detector.py <path_to_audio_file> <path_to_output_txt_file>")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    output_file = sys.argv[2]
    detect_beats(audio_file, output_file)

# Example usage within the script (if not using command line arguments)
# detect_beats("path/to/your/music.wav", "path/to/your/beat_timestamps.txt")