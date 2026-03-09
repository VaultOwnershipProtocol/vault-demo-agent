```python
from vault_ai import connect_vault

def run_agent():

    vault = connect_vault("user_123")

    passport = vault.request_passport(
        agent_id="planning-agent",
        scopes=["preferences", "projects"],
        purpose="Provide personalized weekly planning"
    )

    print("Passport request:")
    print(passport)

    context = vault.get_context(passport)

    print("Retrieved context:")
    print(context)

    print("\nAgent response:\n")

    print(f"""
Hello! Based on your Vault context:

Projects: {context["projects"]}
Preferred tone: {context["preferences"]["tone"]}

Here is your suggested weekly focus:

1. Prioritize work on Vault AI
2. Continue development of the Ownership Layer Manifesto
3. Allocate time for research and planning

This plan was generated using your Vault context.
""")


if __name__ == "__main__":
    run_agent()
