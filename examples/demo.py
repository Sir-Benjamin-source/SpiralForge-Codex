# examples/demo.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TruthLayering import TruthLayer
from NarrativeCoherence import NarrativeEngine
from EthicalFilter import EthicalFilter

def main():
    # Sample input text (e.g., from an LLM)
    sample_text = "The sky is blue."
    
    # Process with TruthLayer
    truth_engine = TruthLayer()
    truth_result = truth_engine.process(sample_text)
    
    # Refine with NarrativeEngine
    coherence_engine = NarrativeEngine()
    coherence_result = coherence_engine.refine(truth_result['enhanced_text'])
    
    # Filter with EthicalFilter
    ethical_filter = EthicalFilter()
    ethical_result = ethical_filter.filter(coherence_result['refined_text'])
    
    # Print results
    print(f"Input: {sample_text}")
    print(f"Truth Output: {truth_result['enhanced_text']}")
    print(f"Truth Score: {truth_result['truth_score']}")
    print(f"Coherence Output: {coherence_result['refined_text']}")
    print(f"Coherence Score: {coherence_result['coherence_score']}")
    print(f"Ethical Output: {ethical_result['filtered_text']}")
    print(f"Ethics Score: {ethical_result['ethics_score']}")
    print(f"Compliance Status: {ethical_result['compliance_status']}")

if __name__ == "__main__":
    main()
