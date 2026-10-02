# Veyra
Veyra is a filesystem-based personal operations and AI-assistant system designed around human-readable state, controlled automation, and explicit security boundaries.
## Current Version
Veyra V0.1
## Current Goal
Use the Veyra V0.1 daily operations runner as the foundation for a controlled LLM interface that can read operational context, propose state changes, and require human approval before modifying user data.
## Current Capabilities
- Filesystem-based, human-readable operational state
- Python daily operations runner
- Parsing of project, task, and waiting-state Markdown files
- Explicit allowlisted file access
- Read-only operation for the current runner
- Fail-safe handling for missing approved files
- Empty-state handling
- Separation of public application logic from private user data
- Requirements, design, and test documentation
- Git-based version control
## Design Principles
- Human-readable source of truth
- Model-agnostic architecture
- Least-privilege access
- Separation of application logic from private user data
- Human approval for consequential actions
- Auditable automation
- Minimal dependencies
