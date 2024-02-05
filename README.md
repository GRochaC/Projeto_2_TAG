# Projeto_2_TAG
Projeto 2 da disciplina "CIC0199 - Teoria e Aplicação de Grafos". 

Para resolver o problema do emparelhamento estável e máximo, proposto pelo projeto, foi-se implementado uma variação do algoritmo Gale-Shapley. 
	
De forma breve, o algoritmo desenvolvido no projeto:
	-Pega um aluno que ainda não foi designado a um projeto;
	-Itera pelos seus projetos de interesse, verificando se ainda há vagas no projeto e se o aluno possui a nota mínima para participar;
	-Caso o i-ésimo projeto o rejeita, é analisado o próximo projeto de seu interesse até que designado a um ou é marcado como rejeitado.
	-Repete o primeiro passo até que todos alunos sejam analisados, assim computando um emparelhamento máximo e estável.
	
A principal variação desse algoritmo, em comparação ao algoritmo original, é no tratamento da substituição do pior aluno do projeto a_ para o aluno a. Essa parte do algoritmo é executada se o projeto em questão esstá cheio e o aluno atende o pré-requisito de nota. Com isso, itera-se pelos alunos presentes no projeto e procura-se pelo pior aluno. Ao localizá-lo, se verifica se a nota do pior aluno é menor ou igual à nota do aluno a ser adicionado no projeto. No case de:
	-nota do pior aluno menor que a nota do aluno: o pior aluno é substituído;
	-nota do pior aluno igual à nota do aluno: se o pior aluno tiver uma preferência ao projeto estritamente menor que a preferência do aluno, ele é substituído.
	
Após computar o emparelhamento, o arquivo "saidaProj2Tag.txt" é gerado, contendo os logs das iterações e emparelhamentos, assim como os pares Projetos x Alunos finais.
