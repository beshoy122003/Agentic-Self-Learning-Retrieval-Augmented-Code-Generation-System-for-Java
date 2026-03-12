from app.agents.writer_agent import writer_agent

state = {

"query":"write java function to reverse string",

"plan":"1 understand the problem 2 generate java method",

"context":[
"public String reverse(String s){ return new StringBuilder(s).reverse().toString(); }"
]

}

result = writer_agent(state)

print(result["generated_code"])