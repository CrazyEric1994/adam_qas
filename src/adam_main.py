
import question_decompose

input_question = "How can there be any sin in sincere? Where is the good in goodbye?"

qd_phase = question_decompose.QuestionDecompose(input_question)
question = qd_phase.segment_sentence()
print(question)
