from app.agents.critic_agent import critic_agent

state = {

"generated_code":
"""
public class Test {

public static String reverse(String s){
return new StringBuilder(s).reverse().toString();
}

}
"""
}

result = critic_agent(state)

print(result)