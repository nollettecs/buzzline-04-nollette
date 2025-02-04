# buzzline-04-nollette
# Cole Nollette
   - 2/4/25
   - 44-671 Module 4

## Building visualizations into our Consumer

We can analyze and visualize different types of streaming data as the information arrives.

### **New Enhancements in the Custom Producer and Consumer**

In this version of Buzzline, we have made significant enhancements to both the **producer** and **consumer**:

1. **Custom JSON Producer**:
   - Generates random messages with dynamically assigned **categories** based on **keywords**.
   - Assigns a **sentiment score** to each message (stub function for now).
   - Streams data to both a file (`project_live.json`) and a Kafka topic if available.
   - Includes error handling for Kafka connectivity issues.

2. **Custom JSON Consumer with Live Pie Chart**:
   - Consumes messages from Kafka in **real-time**.
   - Extracts **category** from each message and dynamically updates a **pie chart** to visualize category distribution.
   - Uses **Matplotlib's animation capabilities** to ensure real-time visualization updates.
   - Manages a **dictionary structure (`category_counts`)** to efficiently count and update category occurrences.

These enhancements provide better insights into the streaming data and make it easier to visualize trends dynamically.

---

## This project uses matplotlib and its animation capabilities for visualization. 

It generates three applications:

1. A basic producer and consumer that exchange information via a dynamically updated file. 
2. A JSON producer and consumer that exchange information via a Kafka topic. 
3. A CSV producer and consumer that exchange information via a different Kafka topic. 

All three applications produce live charts to illustrate the data. 

## Task 1. Use Tools from Module 1 and 2

Before starting, ensure you have completed the setup tasks in <https://github.com/denisecase/buzzline-01-case> and <https://github.com/denisecase/buzzline-02-case> first. 
Python 3.11 is required. 

## Task 2. Copy This Example Project and Rename

Once the tools are installed, copy/fork this project into your GitHub account
and create your own version of this project to run and experiment with. 
Follow the instructions in [FORK-THIS-REPO.md](https://github.com/denisecase/buzzline-01-case/docs/FORK-THIS-REPO.md).

OR: For more practice, add these example scripts or features to your earlier project. 
You'll want to check requirements.txt, .env, and the consumers, producers, and util folders. 
Use your README.md to record your workflow and commands. 
    

## Task 3. Manage Local Project Virtual Environment

Follow the instructions in [MANAGE-VENV.md](https://github.com/denisecase/buzzline-01-case/docs/MANAGE-VENV.md) to:
1. Create your .venv
2. Activate .venv
3. Install the required dependencies using requirements.txt.

## Task 4. Start Zookeeper and Kafka (2 Terminals)

If Zookeeper and Kafka are not already running, you'll need to restart them.
See instructions at [SETUP-KAFKA.md] to:

1. Start Zookeeper Service ([link](https://github.com/denisecase/buzzline-02-case/blob/main/docs/SETUP-KAFKA.md#step-7-start-zookeeper-service-terminal-1))
2. Start Kafka ([link](https://github.com/denisecase/buzzline-02-case/blob/main/docs/SETUP-KAFKA.md#step-8-start-kafka-terminal-2))

---

## Task 5. Start a Basic (File-based, not Kafka) Streaming Application

This will take two terminals:

1. One to run the producer which writes to a file in the data folder. 
2. Another to run the consumer which reads from the dynamically updated file. 

### Producer Terminal

Start the producer to generate the messages. 

In VS Code, open a NEW terminal.
Use the commands below to activate .venv, and start the producer. 

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m producers.basic_json_producer_case
```

### Consumer Terminal

Start the associated consumer that will process and visualize the messages. 

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and start the consumer. 

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.basic_json_consumer_case
```

### Review the Application Code

Review the code for both the producer and the consumer. 
Understand how the information is generated, written to a file, and read and processed. 
Review the visualization code to see how the live chart is produced. 
When done, remember to kill the associated terminals for the producer and consumer. 

---

## Task 6. Start a (Kafka-based) JSON Streaming Application

This will take two terminals:

1. One to run the producer which writes to a Kafka topic. 
2. Another to run the consumer which reads from that Kafka topic.

For each one, you will need to: 
1. Open a new terminal. 
2. Activate your .venv.
3. Know the command that works on your machine to execute python (e.g. py or python3).
4. Know how to use the -m (module flag to run your file as a module).
5. Know the full name of the module you want to run. 
   - Look in the producers folder for json_producer_case.
   - Look in the consumers folder for json_consumer_case.

### Review the Application Code

Review the code for both the producer and the consumer. 
Understand how the information is generated and written to a Kafka topic, and consumed from the topic and processed. 
Review the visualization code to see how the live chart is produced. 

Compare the non-Kafka JSON streaming application to the Kafka JSON streaming application.
By organizing code into reusable functions, which functions can be reused? 
Which functions must be updated based on the sharing mechanism? 
What new functions/features must be added to work with a Kafka-based streaming system?

When done, remember to kill the associated terminals for the producer and consumer. 

---

## Live Chart Examples

Live Bar Chart (JSON file streaming)

![Basic JSON (file-exchange)](images/live_bar_chart_basic_example.jpg)

Live Pie Chart (Kafka JSON streaming)

![JSON (Kafka)](images/live_pie_chart_example.jpg)

Live Line Chart with Alert (Kafka CSV streaming)

![CSV (Kafka)](images/live_line_chart_example.jpg)
