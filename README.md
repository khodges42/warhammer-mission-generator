
# Warhammer Mission Generator

Welcome to the Warhammer Mission Generator! This project provides a tool for generating randomized Warhammer 40k missions, including primary missions, deployment types, and mission rules. We've included some GPT generated missions, but feel free to input your own cards. I won't be including official Games Workshop rules in this repo, but if you edit the missions json file (or create another) with rules that you prefer to play with, you can use those too.

## Features

- **Primary Missions**: Randomly select from a list of primary missions.
- **Deployment Types**: Choose from various deployment types to set up your battlefield.
- **Mission Rules**: Generate and apply mission rules to enhance gameplay with unique conditions.

## Getting Started

To get started with the Warhammer Mission Generator, you'll need to set up the Flask web application. Follow these steps to get up and running:

### Prerequisites

- Python 3.x
- Flask (web framework for Python)
- A modern web browser

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/khodges42/warhammer-mission-generator.git
   cd warhammer-mission-generator
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your JSON File**

   Place your `.json` file in the `missions` directory. Ensure the JSON file is structured according to the expected schema.

5. **Run the Flask App**

   ```bash
   python app.py
   ```

   Your Flask application will start and be accessible at `http://127.0.0.1:5000`.

### Usage

1. **Navigate to the App**

   Open your web browser and go to `http://127.0.0.1:5000`.

2. **Generate Missions**

   Click the "Generate" button to randomly select a primary mission, deployment type, and mission rule. Each selection will be displayed as a card on the page with relevant details.

3. **Re-select Missions**

   Each card has a button to re-select a new random choice for that category.

## JSON Schema

The JSON file (`genericmissions.json`) should contain the following categories:

- **primaryMissions**: List of primary mission objects with `name`, `rule`, and optional `image`.
- **missionRules**: List of mission rule objects with `name`, `rule`, and optional `image`.
- **deployments**: List of deployment objects with `name`, `rule`, and optional `image`.

Example of JSON structure:

```json
{
  "primaryMissions": [
    {
      "name": "Mission Name",
      "rule": "<b>Second Battle Round Onwards</b> <br/> ...",
      "image": ""
    }
  ],
  "missionRules": [
    {
      "name": "Fixed Positions",
      "rule": "Players can target units ...",
      "image": ""
    }
  ],
  "deployments": [
    {
      "name": "Tactical Engagement",
      "rule": "foobar",
      "image": "./static/images/tacticalengagement.jpg"
    }
  ]
}
```

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Contributions are always welcome!



