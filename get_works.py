import json, os
from requests_oauthlib import OAuth1Session

from LINE_notify import post_line_notify


def main():

    SN = os.environ.get('SECRET_NAME','')

    ### Load all tweet from log file
    with open('out.json', 'r') as f:
        data = json.load(f)


    ### Pickup only work tweet
    all_works = {'id': []}
    with open('tags.json', 'r') as f:
        search_tags = json.load(f)

    for d in data:

        """Pick up on the condition that...
        * specific hashtag is attached
        * not reply for myself
        * not retweet of other
        """

        hashtags = d['entities']['hashtags']
        is_self_reply = d['in_reply_to_screen_name'] == SN
        is_other_retweet = False
        if 'retweeted_status' in d:
            is_other_retweet = not d['retweeted_status']['user']['screen_name'] == SN

        if len(hashtags) > 0 and (not is_other_retweet) and (not is_self_reply):
            tag = hashtags[0]['text']
            if tag in search_tags:
                # print('id: ' + d['id_str'])
                # print('text: \n' + d['full_text'])
                # print('------')
                all_works['id'].append(d['id'])

    # print("------------------------------------")
    # print("all_works: " + str(len(all_works['id'])))


    ### Save id list
    with open('work.json', 'w') as f:
        json.dump(all_works, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


    ### Post to LINE-Notify
    post_line_notify('Updated all works file.')


if __name__ == "__main__":
    main()