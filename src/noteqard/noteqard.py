import openai

def text_to_question_answer(text:str) -> list[dict[str, str]]:
    example_text = """
    The blood circulatory system is a system of organs that includes the heart, blood vessels, and blood which is circulated throughout the entire body of a human or other vertebrate.[1][2] It includes the cardiovascular system, or vascular system, that consists of the heart and blood vessels (from Greek kardia meaning heart, and from Latin vascula meaning vessels). The circulatory system has two divisions, a systemic circulation or circuit, and a pulmonary circulation or circuit.[3] Some sources use the terms cardiovascular system and vascular system interchangeably with the circulatory system.[4]
    """

    example_response = """
    Q: What is the blood circulatory system and what does it include?
    A: The blood circulatory system is a system of organs that includes the heart, blood vessels, and blood.

    Q: What are the two divisions of the circulatory system?
    A: The two divisions of the circulatory system are systemic circulation and pulmonary circulation.

    Q: What are the main components of blood?
    A: The main components of blood are plasma, red blood cells, white blood cells, and platelets.

    Q: What is the function of the circulatory system?
    A: The function of the circulatory system is to circulate blood throughout the body, carrying oxygen and nutrients to the tissues and removing waste materials.

    Q: What is the role of the lymphatic system in relation to the circulatory system?
    A: The lymphatic system is complementary to the circulatory system and carries excess plasma away from the body tissues, returning it back to the blood circulation as lymph.

    Q: How does the lymphatic system work?
    A: The lymphatic system works by filtering excess interstitial fluid and returning it to the blood circulation as lymph.

    Q: What are some medical professionals specializing in the circulatory system?
    A: Cardiologists specialize in the heart, cardiothoracic surgeons operate on the heart and surrounding areas, and vascular surgeons focus on disorders of the blood vessels and lymphatic vessels.
    """
    
    result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    presence_penalty=-.5,
    messages=[
        {"role": "system", "content": "You are rephrasing the text I give you into question and answers so that they can be used for flashcard studying."},
        {"role": "user", "content": example_text},
        {"role": "assistant", "content": example_response},
        {"role": "user", "content": text},
    ]
    )
    output = []
    
    qas = result["choices"][0]["message"]["content"]
    qas = qas.split("\n\n")
    for qa in qas:
        q, a = qa.split("\nA:")
        a = "A:"+a
        output.append({"Q":q, "A":a})
    
    return output

def qa_to_anki_importable(qas:list[dict[str, str]]) -> str:
    output = "Question\tAnswer\n"
    for qa in qas:
        output += qa["Q"] + "\t" + qa["A"] + "\n"
    return output

def export_qa_to_tsv(fn:str, qas:list[dict[str,str]]) -> None:
    with open(fn, "w") as fout:
        output = qa_to_anki_importable(qas)
        fout.write(output)