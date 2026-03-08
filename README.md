# Web Activity Agent System

An intelligent multi-agent system that converts natural language questions into SQL queries and provides insightful responses about web activity and GitHub data. Built with OpenAI, MySQL, FastAPI, and Streamlit.

**📚 For comprehensive documentation, see [docs/DOCUMENTATION.md](docs/DOCUMENTATION.md)**

## Features

- **Multi-Agent Architecture**: Specialized agents for schema awareness, SQL generation, query execution, and response formatting
- **OpenAI Models**: Powered by OpenAI chat models
- **MySQL Database**: Robust data storage with proper indexing
- **FastAPI**: Modern backend with REST API and Swagger UI
- **Streamlit Frontend**: Interactive chatbot interface with dark mode
- **Security Guards**: Multi-layer security for query validation and response sanitization
- **Database Schema Awareness**: Dynamic schema discovery and context injection
- **Data Visualization**: Automatic chart generation (bar charts, line charts)
- **LangSmith Tracing**: Observability and debugging support
- **Read-Only Database**: Secure, read-only data access

## Architecture

### Multi-Agent System

```
User Question → SchemaAwarenessAgent → SQLGenerationAgent → QueryExecutionAgent → ResponseFormattingAgent → Natural Response
```

### Core Components

- **LLMDatabaseAgent**: Main orchestrator managing agent flow
- **SchemaAwarenessAgent**: Discovers database structure and sample data
- **SQLGenerationAgent**: Converts natural language to SQL using OpenAI
- **QueryExecutionAgent**: Safely executes SQL queries on MySQL
- **ResponseFormattingAgent**: Converts results to natural language
- **Security Guards**: Query validation and response sanitization
- **Database Manager**: Safe database operations with connection pooling
- **API Endpoints**: REST API (FastAPI) for agent interaction
- **Streamlit UI**: Interactive chatbot with visualizations

## Quick Start

### Prerequisites

- Python 3.13+
- MySQL 8.0+
- OpenAI API key
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Group---K
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp env.example .env
   # Edit .env with your credentials
   ```

5. **Set up database**
   ```bash
   python setup_database.py
   ```

6. **Start the backend server**
   ```bash
   python main.py  # FastAPI on port 8000 with Swagger UI
   # Or: python scripts/start_fastapi.py
   ```

7. **Start the frontend (in a new terminal)**
   ```bash
   python streamlit_app.py  # Streamlit on port 8501
   # Or: streamlit run streamlit_app.py
   # Or: python scripts/start_streamlit.py
   ```

**Access Points**:
- FastAPI + Swagger: `http://localhost:8000/docs`
- Streamlit UI: `http://localhost:8501`

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Database Configuration
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=web_activity_db

# OpenAI API
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini

# LangSmith Configuration (Optional)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=web-activity-agent

# Application Configuration
API_PORT=8000
DEBUG=true
```

## API Endpoints

### System Endpoints
- `GET /` - System information
- `GET /api/health` - Basic health check
- `GET /api/status` - System status

### Agent Endpoints
- `POST /api/agent/ask` - Ask natural language questions
- `POST /api/agent/validate-query` - Validate SQL queries
- `GET /api/agent/health` - Agent health check
- `GET /api/agent/info` - Agent information
- `GET /api/agent/examples` - Query examples

### Traditional API Endpoints
- `POST /api/store_web_activity` - Store web activity data
- `GET /api/get_activity` - Get activity data
- `GET /api/get_user_stats` - Get user statistics
- `POST /api/store_github_activity` - Store GitHub activity
- `GET /api/get_github_activity` - Get GitHub activity
- `GET /api/get_github_stats` - Get GitHub statistics

## Usage Examples

### Natural Language Queries

```bash
# Ask a question about web activity
curl -X POST http://127.0.0.1:8000/api/agent/ask \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Show my web activity for today",
    "user_id": 1
  }'

# Ask about GitHub activity
curl -X POST http://127.0.0.1:8000/api/agent/ask \
  -H "Content-Type: application/json" \
  -d '{
    "question": "How much time did I spend on social media this week?",
    "user_id": 1
  }'

# Ask about repository activity
curl -X POST http://127.0.0.1:8000/api/agent/ask \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are my most active GitHub repositories?",
    "user_id": 1
  }'
```

### Traditional API Usage

```bash
# Store web activity
curl -X POST http://127.0.0.1:8000/api/store_web_activity \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "website_name": "github.com",
    "time_spent": 30,
    "activity_date": "2024-10-25"
  }'

# Get daily activity
curl "http://127.0.0.1:8000/api/get_activity?user_id=1&date=2024-10-25"
```

## Project Structure

```
.
├── main.py                        # FastAPI entry point
├── streamlit_app.py               # Streamlit UI
├── config.py                      # Configuration management
├── env.example                    # Environment template
├── requirements.txt               # Python dependencies
├── setup_database.py              # Database setup script
├── README.md                      # This file
├── docs/                          # Documentation
│   ├── DOCUMENTATION.md
│   └── ARCHITECTURE_DIAGRAM.md
├── scripts/                       # Startup helpers
│   ├── start_fastapi.py
│   └── start_streamlit.py
├── tests/                         # Test scripts
│   └── test_union_queries.py
├── agents/                        # LLM Agent System
│   ├── core/                      # Core agent components
│   │   ├── prompt_manager.py
│   │   └── llm_agent.py
│   ├── guards/                    # Security components
│   │   └── security_guards.py
│   └── prompts/                   # Jinja2 templates
│       ├── sql_generation.j2
│       ├── response_formatting.j2
│       └── query_validation.j2
└── backend/                       # Backend components
    └── database/
        └── db_manager.py
```

## Security Features

### Multi-Layer Security

1. **Query Validation**: Blocks dangerous SQL operations
2. **User ID Filtering**: Ensures all queries include user_id filtering
3. **LLM Validation**: Additional AI-powered query validation
4. **Response Sanitization**: Cleans LLM responses for security
5. **Input Validation**: Validates all user inputs

### Blocked Operations

- DROP, DELETE, UPDATE, INSERT, ALTER, CREATE
- System table access
- Multiple statement execution
- Non-standard SQL keywords (in high security mode)

## Database Schema

### web_activity Table

| Column | Type | Description |
|--------|------|-------------|
| id | INT AUTO_INCREMENT PRIMARY KEY | Auto-incrementing primary key |
| user_id | INT NOT NULL | User identifier |
| website_name | VARCHAR(255) NOT NULL | Name of the website |
| time_spent | INT NOT NULL | Time spent in minutes |
| activity_date | DATE NOT NULL | Date of the activity |
| created_at | TIMESTAMP | Record creation timestamp |

### github_activity Table

| Column | Type | Description |
|--------|------|-------------|
| id | INT AUTO_INCREMENT PRIMARY KEY | Auto-incrementing primary key |
| user_id | INT NOT NULL | User identifier |
| github_username | VARCHAR(255) NOT NULL | GitHub username |
| activity_type | ENUM | Type of activity (commit, pull_request, issue, push, repository) |
| repository_name | VARCHAR(255) | Repository name |
| activity_description | TEXT | Description of the activity |
| commit_count | INT DEFAULT 0 | Number of commits |
| activity_date | DATE NOT NULL | Date of the activity |
| created_at | TIMESTAMP | Record creation timestamp |

## Error Handling

The API returns appropriate HTTP status codes:

- `200` - Success
- `201` - Created
- `400` - Bad Request (validation errors)
- `404` - Not Found
- `405` - Method Not Allowed
- `500` - Internal Server Error

## Development

### Running the Application

```bash
# Start the full system
python main.py
```

### Testing the Agent

```bash
# Test agent health
curl http://127.0.0.1:8000/api/agent/health

# Get agent information
curl http://127.0.0.1:8000/api/agent/info

# Get query examples
curl http://127.0.0.1:8000/api/agent/examples
```

## Quick Reference

### Running the System

```bash
# Terminal 1: Backend
python main.py

# Terminal 2: Frontend
python streamlit_app.py
```

### Example Questions

1. "How much time did I spend on YouTube today?"
2. "Show me my most active GitHub repositories this week."
3. "What are my top 5 visited websites?"
4. "Compare my GitHub activity vs web browsing time."
5. "How much time did I spend on social media this month?"

### File Structure

```
.
├── main.py
├── streamlit_app.py
├── setup_database.py
├── docs/
├── scripts/
├── tests/
├── agents/
└── backend/
```

## Support

For issues and questions:
- 📖 See [docs/DOCUMENTATION.md](docs/DOCUMENTATION.md) for comprehensive guide
- 🐛 Create an issue on GitHub
- 📧 Email: support@example.com

## License

MIT License
