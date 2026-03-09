# vault-demo-agent
Example AI agent using Vault context.
# Vault Demo Agent

Example AI agent using the Vault SDK to retrieve user-owned context.

This repository demonstrates how an AI agent can request and use personal context through the Vault Context Protocol.

---

## Overview

Most AI systems start without any understanding of the user.

Vault introduces a permissioned context layer that allows AI agents to access user-owned data such as:

- preferences
- projects
- goals
- knowledge

This demo shows a simple agent retrieving context from Vault.

---

## Example Flow

User connects their Vault.

The agent requests permission to access context.

Vault issues a Vault Passport.

The agent retrieves approved context and uses it to personalize responses.

---

## Example Agent

Example code:

```python
from vault_ai import connect_vault

vault = connect_vault("user_123")

passport = vault.request_passport(
    agent_id="planning-agent",
    scopes=["preferences", "projects"],
    purpose="Provide personalized weekly planning"
)

context = vault.get_context(passport)

print("User context:", context)

print("Planning week using Vault context...")
Why This Matters

AI models provide intelligence.

Vault provides ownership and context.

Together they enable truly personal AI systems.

License

MIT License

Copyright 2026 Byron Goodman
