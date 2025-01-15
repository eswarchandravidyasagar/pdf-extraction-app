# PDF Data Extraction Tool

This project is a web-based application for extracting structured data from PDF files using GPT-4 and Python. The application allows users to upload PDF files, extracts text from them, preprocesses the text, and uses GPT-4 to identify and extract specific data points. The extracted data is then displayed on the web interface and can be downloaded in a structured format like JSON or CSV.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/githubnext/workspace-blank.git
    cd workspace-blank
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up OpenAI API key:
    - Sign up on the OpenAI website and get your API key.
    - Create a `.env` file in the root directory of the project and add your API key:
        ```
        OPENAI_API_KEY=your_api_key_here
        ```

5. Run the application:
    ```bash
    flask run
    ```

## Usage Instructions

1. Open your web browser and go to `http://127.0.0.1:5000/`.

2. Upload a PDF file using the provided form.

3. The application will extract text from the PDF, preprocess it, and use GPT-4 to identify and extract specific data points.

4. The extracted data will be displayed on the web interface.

5. You can download the extracted data in a structured format like JSON or CSV.
