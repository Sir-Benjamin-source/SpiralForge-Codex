# examples/demo.py
from TruthLayering import TruthLayer

def main():
    # Sample input text (e.g., from an LLM)
    sample_text = "The sky is blue."
    
    # Initialize TruthLayer and process text
    truth_engine = TruthLayer()
    result = truth_engine.process(sample_text)
    
    # Print results
    print(f"Input: {sample_text}")
    print(f"Output: {result['enhanced_text']}")
    print(f"Truth Score: {result['truth_score']}")

if __name__ == "__main__":
    main()
