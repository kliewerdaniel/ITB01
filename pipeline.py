# pipeline.py
class NarrativePipeline:
 def run(self, image_path):
     # Step 1: Image Analysis
     analyzer = MultimodalAnalyzer()
     analysis = analyzer.analyze(image_path)
        
     # Step 2: Initialize RAG
     rag = NarrativeRAG()
     rag.index_context(
         document=analysis.json(),
         metadata={"type": "initial_analysis"}
     )
        
     # Step 3: Generate Story
     story = []
     summary = ""
     for chapter_num in range(1, 6):
         context = {
             "current_chapter": chapter_num,
             "summary": summary,
             "mood": analysis.mood,
             "conflicts": analysis.potential_conflicts
         }
            
         chapter = StoryEngine().generate_chapter(context)
         story.append(chapter)
            
         if chapter_num % 5 == 0:
             summary = self._summarize_story(story[-5:])
                
     return story

 def _summarize_story(self, chapters):
     summary_prompt = "Summarize this story arc in 3 sentences:"
     return ollama.generate(
         model="deepseek-llm:70b",
         prompt=summary_prompt + "\n".join(chapters)
     )