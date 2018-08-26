# Google Text Normalization Challenge: English Language¶
Text normalization is defined as the process of transforming text into a single canonical form. Normalizing text before storing or processing it, allows for separation of concerns, since input is then guaranteed to be consistent before operations are performed on it.

Text normalization has seen a huge advancement in technology with the implementation of deep neural networks. Advancements in AI and Processing power has enabled us to process enormous amounts of data rapidly learning from them and producing reliable outputs as required.

Google’ text normalization challenge follows the aftermath of a research paper produced by Google researchers Richard Sporat and Navdeep Jaitly. What they have been trying to do is to design a deep neural network to automate the process of text normalization, given a corpus of labeled text data in the order of a few billion words along with their normalized function.

The goal of this research is to produce DNN model which can efficiently translate written format input into readable output. Example: “15/1/1995” to “Fifteenth January Nineteen Ninety-Five.”

According to the research led by Sporat and Jaitly, they have tried training the model using two types of Neural Network.

Text Normalization using LSTM
Attention Based RNN Sequence to Sequence Model
Both of the above models produced a reasonable amount of accuracy but not to an industry ready standard. To further improve the model, google released a huge labeled dataset along with a cash prize on Kaggle with the hopes of the community at large coming up with a better solution.

By doing this, some interesting results are obtained wherein people have used regular expressions to obtain near perfect results. But this is not ideal since there is no machine intelligence involved and the entirety of the code is hard-coded to find values which will most definitely fail when it comes to real world implementation.

Another method which can be used is the XGBoost or Extreme Gradient Boosting method which has quite often proved to be a winning method for many in Kaggle competitions. It operates as a boosted random forest method and has shown comparatively good results. But the real dilemma is to build a pure DNN which can solve this problem effectively and efficiently.

It is for the same reason, I have opted to use a recurrent neural network using LSTM (Long short-term memory) to attempt this task. The implemented model along with their step by step details have been explained below in each stage of the model writtern as comments and Text.
