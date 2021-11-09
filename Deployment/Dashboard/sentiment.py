import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import preprocessing



def app():
    scatter_column, settings_column = st.beta_columns((4, 1))

    st.title("Sentiment Analysis of tweets")
    st.sidebar.title('Some of the options of epilepsy tweets')

    uploaded_file = st.sidebar.file_uploader("Upload your input file") #, type=["CSV"]

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        st.sidebar.subheader("Show random tweets")
        random_tweet = st.sidebar.radio('Select the Sentiment', ('Positive', 'Negative', 'Neutral'))

        st.subheader("Here are some example of tweets according to your choice!")
        st.markdown("1." + data.query("sentiment == @random_tweet")[['Text']].sample(n=2).iat[1, 0])

        st.sidebar.markdown("### Number of tweets")
        select = st.sidebar.selectbox('Visualization Type', ['Histogram', 'PieChart'])

        sentiment_count = data['sentiment'].value_counts()
        sentiment_count = pd.DataFrame({'Sentiments': sentiment_count.index, 'Tweets': sentiment_count.values})

        if st.sidebar.checkbox('Show', False, key='0'):
            st.markdown("### No. of tweets by sentiments ")
            if select == 'Histogram':
                fig = px.bar(sentiment_count, x='Sentiments', y='Tweets', color='Tweets', height=500)
                st.plotly_chart(fig)
            else:
                fig = px.pie(sentiment_count, values='Tweets', names='Sentiments')
                st.plotly_chart(fig)

        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.sidebar.subheader("Word Cloud")
        word_sentiment = st.sidebar.radio("Which Sentiment to Display?", tuple(pd.unique(data["sentiment"])))
        if st.sidebar.checkbox("Show", False, key="6"):
            st.subheader(f"Word Cloud for {word_sentiment.capitalize()} Sentiment")
            df = data[data["sentiment"] == word_sentiment]
            words = " ".join(df["Text"])
            processed_words = " ".join([word for word in words.split() if
                                        "http" not in word and not word.startswith(
                                            "@") and word != "RT" and not word in (
                                            ["epilepsy", "epilepsypositivity", "Epilepsy", "epilepsywarrior", "seizure",
                                             "s"])])
            wordcloud = WordCloud(stopwords=STOPWORDS, background_color="white", width=800, height=340).generate(
                processed_words)
            plt.imshow(wordcloud)
            plt.xticks([])
            plt.yticks([])
            st.pyplot()

        st.sidebar.subheader("scatter plot")
        if st.sidebar.checkbox('Show', False, key='7'):
            st.markdown("###  Polarity and subjectivity scatter")
            fig = px.scatter(data_frame=data, x='Polarity', y='Subjectivity', color='sentiment', height=500)
            st.plotly_chart(fig)
    else:
        scatter_column.header("Please Choose a file")
