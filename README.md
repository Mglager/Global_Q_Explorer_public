# Global Q Explorer

A Streamlit application for exploring and analyzing global factor portfolios.

## Setup Options

You can run this application either locally with Python or using Docker.

### A. Local Python Setup

1. **Prerequisites**
   - Python 3.8 or higher
   - pip (Python package installer)

2. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Global_Q_Explorer.git
   cd Global_Q_Explorer
   ```

3. **Create and Activate Virtual Environment (Recommended)**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

6. **Access the Application**
   - Open your web browser and go to `http://localhost:8501`

### B. Docker Setup

1. **Prerequisites**
   - Docker installed on your system
   - Docker Compose (optional, but recommended)

2. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Global_Q_Explorer.git
   cd Global_Q_Explorer
   ```

3. **Build and Run with Docker Compose (Recommended)**
   ```bash
   docker-compose up --build
   ```

   Or using Docker directly:
   ```bash
   docker build -t global-q-explorer .
   docker run -p 8501:8501 global-q-explorer
   ```

4. **Access the Application**
   - Open your web browser and go to `http://localhost:8501`

## Project Structure

```
Global_Q_Explorer/
├── app.py                 # Main Streamlit application
├── src/                   # Source code
│   ├── analysis.py       # Analysis functions
│   ├── data_loader.py    # Data loading utilities
│   ├── data_processor.py # Data processing functions
│   └── visualizations.py # Visualization functions
├── data/                 # Data directory
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
└── docker-compose.yml   # Docker Compose configuration
```

## Dependencies

The main dependencies are:
- streamlit
- pandas
- numpy
- plotly
- scipy

See `requirements.txt` for the complete list of dependencies.

## Data Requirements

Place your data files in the `data/` directory. The application expects data files in a specific format:
- CSV files with columns including 'date', 'ret_vw', 'ret_ew'
- Files should be organized by factor groups

## Troubleshooting

1. **Port Already in Use**
   - If port 8501 is already in use, Streamlit will automatically try the next available port
   - Check the terminal output for the correct URL

2. **Memory Issues**
   - If you encounter memory issues, try running Python with increased memory limit:
     ```bash
     python -X "max_memory=8G" -m streamlit run app.py
     ```

3. **Docker Issues**
   - If you encounter permission issues with Docker:
     ```bash
     sudo docker-compose up --build
     ```

## Support

For issues and feature requests, please create an issue in the GitHub repository. 