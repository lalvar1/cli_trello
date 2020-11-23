# Author: Luciano Alvarez
# Contact: alvarezluciano1993@gmail.com
import requests
import argparse


class TrelloBuilder:
    """A Class to manage Trello board changes"""

    def __init__(self, api_key, token, board_id):
        self.api_key = api_key
        self.access_token = token
        self.api_url = "https://api.trello.com/1/"
        self.board_id = board_id
        self.board_lists = self.get_board_lists(board_id)

    def create_card(self, name, column_name):
        """
        Create card on {column_name} column
        :param name: card name
        :param column_name: list or column name
        :return: created card id
        """
        query = {
            'key': self.api_key,
            'token': self.access_token,
            'idList': self.get_list_id(column_name),
            'name': name
        }
        response = requests.post(self.api_url + 'cards', params=query)
        print(f'Card {name} on {column_name} column was created successfully')
        return response.json()["id"]

    def add_card_comment(self, comment, card_id):
        """
        Add a comment to a card
        :param comment: Text comment
        :param card_id: card unique id
        :return: None
        """
        query = {
            'key': self.api_key,
            'token': self.access_token,
            'text': comment,
        }
        requests.post(self.api_url + f'cards/{card_id}/actions/comments',
                      params=query)
        print(f'Comment {comment} was added successfully')

    def create_card_label(self, card_id, label_name, label_color):
        """
        Create label on a card
        :param card_id: unique card id
        :param label_name: label name for target label
        :param label_color: label color
        :return: None
        """
        query = {
            'key': self.api_key,
            'token': self.access_token,
            'color': label_color,
            'name': label_name
        }
        requests.post(self.api_url + f'cards/{card_id}/labels',
                      params=query)
        print(f'Label {label_name} was created successfully')

    def get_list_id(self, column_name):
        """
        Get unique id of a given column or list
        :param column_name: name of list/column
        :return: list unique id
        """
        for _list in self.board_lists:
            if _list['name'].upper() == column_name.upper():
                return _list['id']
        return

    def get_board_lists(self, board_id):
        """
        Get all lists on a board
        :param board_id: board unique id
        :return: board's lists
        """
        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': self.api_key,
            'token': self.access_token
        }
        response = requests.get(self.api_url + f'boards/{board_id}/lists',
                                headers=headers, params=query)

        return response.json()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', required=True, help='Trello API Access Token')
    parser.add_argument('--api-key', required=True, help='Trello API Key')
    parser.add_argument('--card-name', required=True, help='New card name')
    parser.add_argument('--board-id', required=True, help='Existent Trello board ID')
    parser.add_argument('--column-name', required=True,
                        help='Column name/list for new card')
    parser.add_argument('--label-name', required=True, help='Label name for new card')
    parser.add_argument('--label-color', required=False,
                        help='Label name for new card. Default=non-color')
    parser.add_argument('--comment', required=True, help='Comment for new card')
    return vars(parser.parse_args())


if __name__ == "__main__":
    args = get_args()
    card_name = args["card_name"]
    column_name = args["column_name"]
    comment = args["comment"]
    api_key = args["api_key"]
    token = args["token"]
    board_id = args["board_id"]
    label_color = args["label_color"]
    label_name = args["label_name"]
    trello_creator = TrelloBuilder(api_key, token, board_id)
    card_id = trello_creator.create_card(card_name, column_name)
    trello_creator.add_card_comment(comment, card_id)
    trello_creator.create_card_label(card_id, label_name, label_color)
