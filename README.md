# Leaf Rice Disease Classification

This repository contains the source code and documentation for the Leaf Rice Disease Classification project, developed as a final project for Agriculture Informatics. The project aims to classify rice leaf diseases using a machine learning model, integrated with a web-based interface for user interaction.

## Project Overview

The Leaf Rice Disease Classification system leverages a trained machine learning model to predict rice leaf diseases based on uploaded images. The application is designed with a user-friendly front-end interface and a robust back-end to handle model predictions. The system is built to assist farmers and agricultural professionals in identifying rice leaf diseases efficiently.

## Mock-Up Design

The front-end design mock-up is available on Figma:  
[View Mock-Up](https://www.figma.com/file/Ld18KowBshaZQiEGkiaFfB/Untitled?node-id=0%3A1&t=ACEYlJqaDMhtVGjd-1)

## Directory Structure

- **model/**: Contains the machine learning model and related scripts.
  - `model.h5`: The trained machine learning model for rice leaf disease classification.
  - `predict.py`: Script to load the model and perform predictions on input data.
- **templates/**: Stores HTML files for the front-end interface.
  - HTML files for rendering the web application.
- **app.py**: The main back-end script that integrates the front-end and the machine learning model, handling requests and predictions.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/leaf-rice-disease-classification.git
   cd leaf-rice-disease-classification
   ```

2. **Install Dependencies**:
   Ensure Python 3.8+ is installed. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Model**:
   Place the trained `.h5` model file in the `model/` directory.

4. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```
   Access the application at `http://localhost:5000` in your web browser.

## Usage

1. Open the web application in a browser.
2. Upload an image of a rice leaf via the provided interface.
3. The system will process the image and display the predicted disease class along with relevant details.

## Technologies Used

- **Back-End**: Python, Flask
- **Front-End**: HTML, CSS, JavaScript
- **Machine Learning**: TensorFlow/Keras (for model development and predictions)
- **Design**: Figma (for UI/UX mock-up)

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries or feedback, please contact:
- Widi Afandi: [widiafandi58@gmail.com](mailto:widiafandi58@gmail.com)
- Satria Nur Saputro: [satrianursaputro06@gmail.com](mailto:satrianursaputro06@gmail.com)