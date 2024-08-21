# Image Classification with HuggingFace and Streamlit

This repository contains a project focused on fine-tuning a pre-trained model from HuggingFace to accurately classify images of birds, cats, and dogs. The project also includes a Streamlit application to demonstrate the model's performance.

### Model and dataset:
- Pre-trained Model: ['akahana/vit-base-cats-vs-dogs'](https://huggingface.co/akahana/vit-base-cats-vs-dogs)
- Dataset: [High-Resolution Cat, Dog, and Bird Image Dataset from Kaggle](https://www.kaggle.com/datasets/mahmoudnoor/high-resolution-catdogbird-image-dataset-13000/data)


### Project Aim:
- Fine-tuning for Multi-class Image Classification (dev.ipynb): This project aims to fine-tune a Vision Transformer (ViT) model to classify images into three categories: birds, cats, and dogs. The fine-tuning process leverages a diverse dataset to enhance the model's accuracy across these classes.

- Interactive Model Testing with Streamlit: The repository includes a Streamlit application (app.py) that provides an interactive interface for testing the fine-tuned model. Users can upload images to see the model's predictions and evaluate its accuracy in real-time.

### How to try out the model using streamlit app.py:
Set Up: Clone the repository and install the requirements.txt.
Run the Streamlit App: 'Execute streamlit run app.py' to launch the Streamlit application.
Use the fine-tuned model: [Ticmate/fine-tuned-cat-dog-bird-model[(https://huggingface.co/akahana/vit-base-cats-vs-dogs)
Upload an Image: Use the app interface to upload an image and view the model's classification.

Example of app.py:
![aae6ba46-a1ae-435b-89dc-00034fbed462](https://github.com/user-attachments/assets/69237f34-94e2-41b2-a153-b748a30ecd30)

