import unittest
from src.main.lab import get_complex_output_parser, invoke_complex_chain, get_complex_prompt

class TestTransform(unittest.TestCase):
    def test_get_complex_prompt(self):
        prompt_template = get_complex_prompt().messages[-1].prompt.template
        self.assertIn("title", prompt_template)
        self.assertIn("is_family_friendly", prompt_template)
        self.assertIn("genre", prompt_template)
        self.assertIn("run_time", prompt_template)
        self.assertIn("year_released", prompt_template)
    
    def test_get_complex_output_parser(self):
        response_schemas = [item.name for item in get_complex_output_parser().response_schemas]
        self.assertIn("title", response_schemas)
        self.assertIn("is_family_friendly", response_schemas)
        self.assertIn("genre", response_schemas)
        self.assertIn("run_time", response_schemas)
        self.assertIn("year_released", response_schemas)
    
    def test_invoke_complex_chain(self):
        try:
            movie = invoke_complex_chain("The Matrix")
        except:
            self.fail("invoke_complex_chain() raised an exception unexpectedly!")
        self.assertIn("title", movie)
        self.assertIn("is_family_friendly", movie)
        self.assertIn("genre", movie)
        self.assertIn("run_time", movie)
        self.assertIn("year_released", movie)

        self.assertIn("The Matrix", movie["title"])
        self.assertIn("Action", movie["genre"])
        self.assertIn("1999", movie["year_released"])
        self.assertIn("136 minutes", movie["run_time"])
        self.assertEqual(False, movie["is_family_friendly"])    

if __name__ == '__main__':
    unittest.main()