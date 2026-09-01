from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.embedder.fastembed import FastEmbedEmbedder
from agno.vectordb.chroma import ChromaDb
from agno.os import AgentOS

import asyncio
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# ============================================================
# BANCO VETORIAL
# ============================================================

vector_db = ChromaDb(
    collection="pdf_agent",
    path="tmp/chromadb",
    persistent_client=True,
    embedder=FastEmbedEmbedder(
        id="BAAI/bge-small-en-v1.5"
    ),
)

# ============================================================
# KNOWLEDGE
# ============================================================

knowledge = Knowledge(
    vector_db=vector_db
)

# ============================================================
# BANCO DE SESSÕES
# ============================================================

db = SqliteDb(
    session_table="agent_session",
    db_file="tmp/agent.db",
)

# ============================================================
# AGENTE
# ============================================================

agent = Agent(
    name="Agente de PDF",

    model=Claude(
        id="claude-sonnet-4-5",
        api_key=os.getenv("ANTHROPIC_API_KEY"),
    ),

    db=db,
    knowledge=knowledge,
    add_history_to_context=True,
    search_knowledge=True,
    debug_mode=True,
)

# ============================================================
# AGENT.OS
# ============================================================

agent_os = AgentOS(
    agents=[agent],
)

app = agent_os.get_app()

# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    asyncio.run(
        knowledge.ainsert(
            url="https://s3.sa-east-1.amazonaws.com/static.grendene.aatb.com.br/releases/2417_2T25.pdf",

            metadata={
                "source": "Grendene",
                "type": "pdf",
                "description": "Relatório Trimestral 2T25",
            },

            skip_if_exists=True,

            reader=PDFReader(),
        )
    )

    agent_os.serve(
        app="exemplo2:app",
        host="0.0.0.0",
        port=7777,
        reload=True,
    )