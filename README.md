# Tool BERT

One of the most exciting aspects of Large Language Models these days is [function calling](https://www.promptingguide.ai/applications/function_calling). To have an interface to ask for up to date information, or complete some request that interacts with another system, is a very real way to help make AI automate away the boring stuff.

However, at least at the time of writing this, function calling is basically only possible with closed source models, at least at a level that is usable. So instead, this repo is meant to be a handicap to help out the smaller / more available models.

This is where Tool-BERT comes in.

Tool-BERT is a fine-tuned version of [BERT](https://huggingface.co/google-bert/bert-base-uncased) for text classification. In particular, the text Tool-BERT can classify is related to the kinds of texts an LLM might encounter that requires function calling.

Obviously, there are a lot of functions an LLM would want to access! At the same time, there are just as many occassions where an LLM does not even require a function call. That's where Tool-BERT helps route these requests before passing to a subsequent LLM, such as is done in [Pi-Card](https://github.com/nkasmanoff/pi-card/blob/main/assistanttools/bert.py).

This repo is structured such that you can make your own Tool-BERT, and then use it in your own projects.

## Getting Started

First, you need to make the dataset! This means figuring out what tools you want your LLM to have access to. To stat, you can take a look at the [tools.py](tools.py) file, containing some of the tools I already thought of.

Once you have your tools, you can use the [make_dataset.py](make_dataset.py) file to create your dataset.

```bash
python make_dataset.py
```

This will create a dataset in the `data` folder, which you can then use to fine-tune your BERT model.

```bash
python train.py
```

This will fine-tune your BERT model, and save it in the `models` folder.

Finally, you can use the [predict.py](predict.py) file to make predictions.

```bash
python predict.py
```

To do all of this, it is currently set up to generate this dataset by using the OpenAI API to generate text. You will need to set up an OpenAI API key, and set it as an environment variable.

```bash
export OPENAI_API_KEY="your-api-key"
```

From there feel free to pick any model you want, and by taking advantage of this large model to make the dataset, fine-tuning Tool-BERT will make it even easier for the smaller models to keep up.

## Next Steps

This was my big idea, but there's so much more to add! I'm honestly not convinced these tools and their descriptions are the best, so please feel free to add more tools, or change the descriptions of the tools.

Also, since the essence of this repo is to avoid closed-source models, if there's a way to replace GPT with a more open model, that would be great!

Finally, the training code here is very basic, so if there's more iteration to do to better track performance and evaluate it, that's also a great next step.
