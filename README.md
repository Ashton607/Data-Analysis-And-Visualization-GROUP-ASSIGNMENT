<h1>NDTA 631: Data Analysis and Visualization</h1>
<h2>Group Project:South African Development Analysis</h2>
<h3>Project Description:</h3>
<p>The project's core objective is to analyze the relationship between female labor force participation 
  and maternal mortality rates in South Africa using two datasets from the World Bank.
  The analysis is performed using Python with the Pandas and Matplotlib libraries
  , and the results are presented through descriptive statistics and a scatter plot visualization.</p>
<h2>Execution Instructions</h2>
<h3>Step 1: Clone the Repository</h3>
<p>Open your terminal or command prompt and clone this repository to your local machine:</p>
<p>git clone [https://github.com/Ashton607/Data-Analysis-And-Visualization-GROUP-ASSIGNMENT.git]
cd Data-Analysis-And-Visualization-GROUP-ASSIGNMENT</p>
<h3>Step 2: Set Up the Environment</h3>
<p>This project requires Python and several libraries. We recommend using a virtual environment to manage dependencies.</p>
<p>1)Create a virtual environment:</p>
<p>python3 -m venv venv</p>
<p>2)Activate the environment:</p>
<p>On macOS/Linux: source venv/bin/activate 

On Windows: venv\Scripts\activate</p>
<p>3) Install libraries</p>
<p>pandas
numpy
matplotlib
openpyxl</p>
<h3>Step 3: Run the Analysis</h3>
<p>Navigate to the src directory and run the main Python script</p>
<p>cd src
python3 data_analysis.py</p>
<h3>Error Handling:</h3>
<p>In your project, the most common errors will be related to file handling and data processing.</p>
<li>
  File Handling (try...except FileNotFoundError):  The load_data function in the provided script uses a try...except block to check if the data files exist in the correct location. If a file is not found, the except block catches the error and prints a helpful message to the user instead of letting the program crash. This is a crucial step for a shared repository where team members might have different file paths.
</li>
<li>
General Exceptions (try...except Exception): The main function wraps the entire data processing and visualization logic in try...except blocks. If something unexpected happens during a complex step—for instance, a data format is incorrect or a calculation fails—the Exception block will catch it and prevent the entire script from failing. It will then print an error message that helps with debugging.
</li>
