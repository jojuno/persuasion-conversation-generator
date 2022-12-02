import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from sklearn.model_selection import train_test_split

# Function to get the persuader, persuadee, and dialogue given a dialogue_id
def get_dialogue(info_df, dialogue_df, dialogue_id):
    participants = info_df[info_df['dialogue_id'] == dialogue_id]
    persuader = participants[participants['role'] == 0]
    persuadee = participants[participants['role'] == 1]
    dialogue = dialogue_df[dialogue_df['dialogue_id'] == dialogue_id]

    return persuader, persuadee, dialogue

# Function that nicely prints a dialogue given a dialogue_id
def print_dialogue(dialogue_id):
    persuader, persuadee, dialogue = get_dialogue(dialogue_id)
    persuader_uid = persuader['uid'].values[0]
    persuadee_uid = persuadee['uid'].values[0]

    title = f"|| Dialogue {dialogue_id} resulted in ${persuader['donation'].values[0]:.2f} being donated ||"
    top_bottom_border = "=" * len(title)
    print(f"{top_bottom_border}\n{title}\n{top_bottom_border}\n")
    
    for _, row in dialogue.iterrows():
        speaker = persuader_uid if row['role'] == 1 else persuadee_uid
        sentence_id = row['sentence_id']
        print(f"[{sentence_id}] [{speaker}]: {row['sentence']}")

def get_donation_stats(info_df):
    donations = info_df['actual_donation']

    min_donation = donations.min()
    median_donation = donations.median()
    max_donation = donations.max()
    avg_donation = donations.mean()
    std_donation = donations.std()

    print(f"Amounts donated:")
    print(f"[Minimum] ${min_donation:.2f}")
    print(f"[Median] ${median_donation:.2f}")
    print(f"[Maximum] ${max_donation:.2f}")
    print(f"[Average] ${avg_donation:.2f}")
    print(f"[Stdev] ${std_donation:.2f}")

    # Probability density function
    pdf = stats.norm.pdf(donations.sort_values(), avg_donation, std_donation)

    # Plot our PDF using different x limits
    plt.plot(donations.sort_values(), pdf)
    plt.xlim([0, 60])
    plt.show()

def report_f1_results(precision, recall, f1, feature_type="No Feature Type Provided", model_type="No Model Type Provided"):
    print(f"{feature_type} Results Using {model_type}:")
    print(f"{format(precision[0], '.2f')}, {format(recall[0], '.2f')}, {format(f1[0], '.2f')}")
    print(f"{format(precision[1], '.2f')}, {format(recall[1], '.2f')}, {format(f1[1], '.2f')}")
    print(f"{format(precision[2], '.2f')}, {format(recall[2], '.2f')}, {format(f1[2], '.2f')}")
    print(f"{format(precision[3], '.2f')}, {format(recall[3], '.2f')}, {format(f1[3], '.2f')}")
    print(f"{format(precision[4], '.2f')}, {format(recall[4], '.2f')}, {format(f1[4], '.2f')}")
    print(f"{format(np.mean(precision), '.2f')}, {format(np.mean(recall), '.2f')}, {format(np.mean(f1), '.2f')}\n")

def report_accuracy(accuracy, feature_type="No Feature Type Provided", model_type="No Model Type Provided"):
    print(f"[{feature_type}]\t[{model_type}]\t\tAccuracy: {format(accuracy * 100, '.2f')}%")

def split_data(features, labels):
    test_size = 0.2
    random_state = None
    train_features, test_features, \
        train_labels, test_labels = train_test_split(features, labels, test_size=test_size, random_state=random_state)

    return np.array(train_features), np.array(test_features), \
        np.array(train_labels), np.array(test_labels)