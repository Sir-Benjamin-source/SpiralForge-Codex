# Hybrid Context Anchor Template

**Purpose**: Human-led with LLM backup; balances speed and depth.

**Execution**:
1. **Human Phase** (30s): Trigger + recall (use AIS: "Steer to 3 core facts").
2. **If Stuck**: Fallback to LLM chain (paste hybrid prompt from llm_chain.md).
3. **Close**: Apply output; stamp version (link Version-Checker+: DOI 10.5281/zenodo.16740228).
4. **Audit**: Log tilt type/outcome.

**Linked Anchors**:
- AIS: [DOI: 10.5281/zenodo.15176494]
- HHL/Flowscript: Logic + flow [DOIs: 10.5281/zenodo.17468251, 10.5281/zenodo.16585562]

**Test Harness**: Notebook stub—run tilts, time recovery.

MIT/CC0.
