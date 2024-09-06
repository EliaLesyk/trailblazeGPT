 # Building GPT Step-by-Step

This repository contains a series of Jupyter notebooks that guide you through the process of building a Generative Pre-trained Transformer (GPT) model from scratch. The tutorial is designed to be accessible to a wide audience, with some mathematical simplifications to enhance understanding.

## Repository Structure

```
.
├── data/
├── helpers/
├── .gitignore
├─1_Setup.ipynb
├─2_Tokenization.ipynb
├─3_Attention.ipynb
├─4_GPT.ipynb
├─5_Training.ipynb
└── requirements.txt
```

## Notebook Flow

The notebooks are designed to be completed in order, each building on the concepts introduced in the previous ones:

1. [**Setup**](1_Setup.ipynb): Introduction to the project with a simple import of DistilGPT2 from Hugging Face to get a basic model running.

2. [**Tokenization**](2_Tokenization.ipynb): Review of tokenization techniques and implementation of a custom dataloader.

3. [**Attention**](3_Attention.ipynb): Deep dive into attention mechanisms, covering:
   - Dot-product attention
   - Scaled attention
   - Attention masks
   - Multi-head attention

4. [**GPT Architecture**](4_GPT.ipynb): Building the core GPT model, including:
   - Multi-Head Attention
   - Layer Normalization
   - Feed-Forward Neural Network
   - Residual Connections

5. [**Training**](5_Training.ipynb): Putting it all together - training, evaluating, and experimenting with hyperparameters.

## How to Use This Repository

Each notebook contains cells marked with `TODO`. These are points where you're encouraged to implement key components of the GPT architecture, helping to reinforce your understanding of how the model works.

To get the most out of this tutorial:
1. Clone the repository
2. Install the required dependencies (listed in `requirements.txt`)
3. Work through the notebooks in order, completing the `TODO` sections
4. Experiment with the code and hyperparameters to deepen your understanding

## Prerequisites

- Basic understanding of Python and PyTorch
- Familiarity with neural network concepts
- Jupyter Notebook environment

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Elina Lesyk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Acknowledgments

This tutorial is designed to make understanding GPT accessible to a wider audience. While some mathematical concepts have been simplified, the core principles of the GPT architecture are preserved.

Happy learning, and enjoy building your own GPT model!
