# Overview
**Trello.py** CLI program, will create a new card on the specified board and column/list, 
with the desired label and comment on it.

## Prerequisites
- Trello account
- Atlassian developer API key and Token
- Trello existent board and column
- Python

## How to run
python -m pip install -r requirements.txt

python trello.py --help

python trello.py --token {token} --api-key {api-key} --card-name {name} 
--board-id {id} --column-name {column} --label-name {label}
--label-color {color} --comment {comment}

Available label colors:
- green
- yellow
- orange
- red
- purple
- blue
- sky 
- lime
- pink
- black

## Potential Improvements
- More functionalities/methods to allow creating more objects on Trello
- Error Handling
- Unittests
- Logging --> Metrics for boards
