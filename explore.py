import nltk
import unicodedata
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

#------------------------------------------------------------------------------------------------------------------------------------------------------

def show_counts_and_ratios(git_repos, column):
    """
    This fucntion takes in a df and column name.
    Will produce a valuecounts for each label and the percetage of the data it represents
    """
    labels = pd.concat([git_repos.language.value_counts(),
                        git_repos.language.value_counts(normalize=True)], axis=1)
    labels.columns = ['n', 'percent']
    
    return labels

show_counts_and_ratios = show_counts_and_ratios(git_repos, 'language')

#------------------------------------------------------------------------------------------------------------------------------------------------------

def plot_clouds(all_words, python_words, java_words):
    
    all_cloud = WordCloud(background_color='white', height=1000, width=400).generate(' '.join(all_words))
    python_cloud = WordCloud(background_color='white', height=600, width=800).generate(' '.join(python_words))
    java_cloud = WordCloud(background_color='white', height=600, width=800).generate(' '.join(java_words))

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.5, .5, .5, .5]), plt.axes([.5, 0, .5, .5])]

    axs[0].imshow(all_cloud)
    axs[1].imshow(python_cloud)
    axs[2].imshow(java_cloud)

    axs[0].set_title('All Words')
    axs[1].set_title('python')
    axs[2].set_title('java')

    for ax in axs: ax.axis('off')
          #------------------------------------------------------------------------------------------------------------------------------------------------------

def words_counted(word_counts):
    
    word_counts = (word_counts
    [(word_counts.java > 10) & (word_counts.python > 10)]
    .assign(ratio=lambda df: df.java / (df.python + .01))
    .sort_values(by='ratio')
    .pipe(lambda df: pd.concat([df.head(), df.tail()])))
    
    return word_counts

#------------------------------------------------------------------------------------------------------------------------------------------------------

def plot_languages(show_counts_and_ratios):
    
    plt.figure(figsize=(10,10))
    sns.set(style="darkgrid")
    plt.title("Types of Code Used (%)", size=20, color='black')
    splot = sns.barplot(x=show_counts_and_ratios.percent, y=show_counts_and_ratios.index, palette='Greens_d', edgecolor='black')
    cnt=0
    for p in splot.patches:
        splot.annotate("%.4f" % p.get_width(), xy=(p.get_width(), p.get_y()+p.get_height()/2),
                xytext=(5, 0), textcoords='offset points', ha="left", va="center")
    plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------------------
    
def all_words_cloud(all_words):
    '''takes in words found in java script readme files
    creates a word cloud out of the words on their own'''
    # make js_words into string format
    all_words = ' '.join(all_words)
    #plt.figure(figsize=(16,8))
    # set the mask to change the shape
    mask = np.array(Image.open('/Users/liamjackson/Desktop/masks/rocket4.png'))
    # create the word cloud
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color="white", contour_width=10, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate(all_words)
    plt.imshow(img)
    plt.axis('off')
    
#------------------------------------------------------------------------------------------------------------------------------------------------------

def java_words_cloud(java_words):
    '''takes in words found in java script readme files
    creates a word cloud out of the words on their own'''
    # make js_words into string format
    all_words = ' '.join(java_words)
    #plt.figure(figsize=(16,8))
    # set the mask to change the shape
    mask = np.array(Image.open('/Users/liamjackson/Desktop/masks/java.png'))
    # create the word cloud
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color="white", contour_width=10, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate(java_words)
    plt.imshow(img)
    plt.axis('off')

#------------------------------------------------------------------------------------------------------------------------------------------------------

def python_words_cloud(python_words):
    '''takes in words found in java script readme files
    creates a word cloud out of the words on their own'''
    # make js_words into string format
    all_words = ' '.join(python_words)
    #plt.figure(figsize=(16,8))
    # set the mask to change the shape
    mask = np.array(Image.open('/Users/liamjackson/Desktop/masks/python.png'))
    # create the word cloud
    img = WordCloud(background_color="black", mask=mask, max_words=1000, 
                    contour_color="white", contour_width=10, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate(python_words)
    plt.imshow(img)
    plt.axis('off')

#------------------------------------------------------------------------------------------------------------------------------------------------------