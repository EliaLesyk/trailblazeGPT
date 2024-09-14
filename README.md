# 🌟 Welcome, LLM Trailblazers! Let's Build Your LLMs Ground Up 🌟

This repository is dedicated to all Trailblazers embarking on the journey to build Large Language Models from the ground up and apply them to their projects. Here you will find a series of Jupyter notebooks that guide you through the process of building a Generative Pre-trained Transformer model from scratch.

## 🌳 Repository Structure

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

## 🛠️ Notebooks and Flow

The notebooks are designed to be completed in order, each building on the concepts introduced in the previous ones:

| Notebook | Description | Open in Colab |
| -------- | ----------- | ------------- |
| 🏁 **Setup** | Introduction to the project, importing DistilGPT2 for a basic model. | [Open In Colab](https://colab.research.google.com/github/EliaLesyk/trailblazeGPT/blob/main/1_Setup.ipynb) |
| ✂️ **Tokenization** | Overview of tokenization techniques and custom dataloader implementation. | [Open In Colab](https://colab.research.google.com/github/EliaLesyk/trailblazeGPT/blob/main/2_Tokenization.ipynb) |
| 🧠 **Attention** | Deep dive into attention mechanisms, such as dot-product, scaled attention, and multi-head attention. | [Open In Colab](https://colab.research.google.com/github/EliaLesyk/trailblazeGPT/blob/main/3_Attention.ipynb) |
| 🏗️ **GPT Architecture** | Build the core GPT model, including Multi-Head Attention, Layer Normalization, Feed-Forward Neural Network, and Residual Connections. | [Open In Colab](https://colab.research.google.com/github/EliaLesyk/trailblazeGPT/blob/main/4_GPT.ipynb) |
| 🎓 **Training** | Train, evaluate, and experiment with hyperparameters for the GPT model. | [Open In Colab](https://colab.research.google.com/github/EliaLesyk/trailblazeGPT/blob/main/5_Training.ipynb) |


## 🎉 Get Started

Clone the repository and explore the notebooks to learn how to build and train your own LLMs!

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

## Acknowledgments

This tutorial is designed to make understanding GPT accessible to a wider audience. While some mathematical concepts have been simplified, the core principles of the GPT architecture are preserved.

Happy learning, and enjoy building your own GPT model!

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🔗 Connect with Me

- [LinkedIn](https://www.linkedin.com/in/elina-lesyk/)
- [X (Twitter)](https://x.com/elesyk)
- [Website](https://elinalesyk.com/)


## 📚 Foundational Papers

To deepen your understanding of LLMs and related technologies, I can't but recommend exploring these foundational papers (each and every time finding something new!):

These papers provide valuable insights into the development, scaling, and optimization of large language models and related AI technologies. 

- **It All Starts Here**
  - ["Attention Is All You Need" (2017)](https://arxiv.org/abs/1706.03762) - Introduces the Transformer architecture, the basis of GPT models.
  - ["Improving Language Understanding by Generative Pre-Training" (2018)](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) - Describes the original GPT model and its benefits.

- **Evolution of GPT Models**
  - ["Language Models are Unsupervised Multitask Learners" (2019)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) - Describes GPT-2.
  - ["Language Models are Few-Shot Learners" (2020)](https://arxiv.org/abs/2005.14165) - Discusses GPT-3's capabilities.
  - ["BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" (2019)](https://arxiv.org/abs/1810.04805) - Explores BERT's impact on the NLP field.

- **Language Models and Scaling**
  - [Scaling Laws for Neural Language Models](https://arxiv.org/pdf/2001.08361)
  - [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/pdf/1909.08053)

- **Instruction Fine-Tuning and Feedback Loops**
  - [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/pdf/2203.02155)
  - ["InstructGPT: Training Language Models to Follow Instructions with Human Feedback" (2022)](https://arxiv.org/abs/2203.02155).
  - ["LoRA: Low-Rank Adaptation of Large Language Models" (2021)](https://arxiv.org/abs/2106.09685) - Introduces a novel approach to fine-tuning large language models efficiently by adding trainable low-rank matrices to the existing weights.
  - ["Training Compute-Optimal Large Language Models" (2022)](https://arxiv.org/abs/2203.15556) - Provides new insights on scaling laws for language models, suggesting that increasing data size and reducing model size can lead to better performance for a given computational budget.

- **Retrieval of Dynamically Changing Knowledge**

  - [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/pdf/2005.11401)

- **Image Synthesis**

  - [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/pdf/2112.10752)

- **System Optimizations**

  - [DeepSpeed: System Optimizations Enable Training Deep Learning Models with Over 100 Billion Parameters](https://dl.acm.org/doi/10.1145/3394486.3406703)
