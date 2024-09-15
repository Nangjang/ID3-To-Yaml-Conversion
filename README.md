# ID3 to YAML Conversion

This repository contains a Python script that reads ID3 metadata from MP3 files in a specified directory and writes the metadata to a YAML file. The metadata includes the title, description, creation date, file path, duration, and file size of each MP3 file.

## Features

- Extracts ID3 metadata from MP3 files.
- Supports reading title and comments from ID3 tags.
- Calculates and formats the duration of the audio file.
- Retrieves and formats the file size.
- Adds the creation date of the audio file.
- Writes the extracted metadata to a YAML file.

## Requirements

- Python 3.x
- `mutagen` library
- `pyyaml` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Nangjang/ID3-To-Yaml-Conversion.git
    cd ID3-To-Yaml-Conversion
    ```

2. Install the required libraries:
    ```sh
    pip install mutagen pyyaml
    ```

## Usage

1. Place your MP3 files in a directory named `audio` within the repository.

2. Run the script:
    ```sh
    python id3-to-yaml-conversion.py
    ```

3. The metadata will be written to a file named `id3-metadata.yaml`.

## Example

Here is an example of the output in `id3-metadata.yaml`:

```yaml
- title: EP01-The Rise of Quantum Computing
  description: Jane Smith and guest Dr. Alice Roberts discuss the breakthroughs in
    quantum computing and what it means for the tech industry in the coming years.
  creation_at: '2024-09-15 15:47:28'
  file: audio\TH01.mp3
  duration: 0:01:00
  length: 482,671
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or suggestions, please contact [Nangjang Kurumbang Subba](mailto:jintrade23@gmail.com).
