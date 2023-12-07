# Swagger File Filter

This Python script filters a Swagger file (either JSON or YAML) to only include specified endpoints and their associated definitions.

## Description

The script reads a Swagger file, filters out the specified endpoints, collects all the definitions used by these endpoints, and writes the filtered Swagger data to a new YAML file.

## How to Start

1. Install the required Python libraries if you haven't already:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the Python script and enter the full path for your Swagger file when prompted. If no path is entered, the script will look for a file named 'swagger.json' in the same directory:
    ```bash
    python script.py --swagger_file path_to_your_swagger_file --endpoints_to_keep /endpoint1 /endpoint2 /endpoint3
    ```

3. The filtered Swagger data will be saved to a new YAML file named 'filtered_swagger.yaml' in the same directory.

## Note

The script currently only supports Swagger files in JSON and YAML formats. Other formats are not supported...
