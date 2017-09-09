<meta charset="UTF-8">

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

# Questão 2: Seja A a matriz de adjacências de um grafo G e k um número natural qualquer. O que representam as entradas da matriz A<sup>k</sup>? Demonstre.

A matriz de adjacência A existe para demonstrar a conexão, ou não, entre vértices de um grafo. Ela funciona da seguinte forma: no espaço A<sub>ij</sub> tem-se a representação de conexão entre os vértices v<sub>i</sub> e v<sub>j</sub>. Se na matriz de adjacência A, o espaço A<sub>ij</sub> tiver seu valor igual a 1, isso diz que existe uma conexão entre os vértices em questão. Esta anotação serve para verificar a conexão de qualquer vértice até qualquer vértice, desde que ambos existam no grafo. Isto inclui a verificação de um vértice para si mesmo.

As entradas da matriz A<sup>k</sup> representam o número de percursos distintos, com tamanho k, existentes entre os vértices v<sub>i</sub> e v<sub>j</sub>.
Demonstrando por indução -> quando k = 1, a matriz de adjacência segue o curso normal, se existir um caminho de tamanho 1 entre os vértices v<sub>i</sub> e v<sub>j</sub> de G. Então:

<h3>
<math xmlns='http://www.w3.org/1998/Math/MathML' display='block'>
    <msup>
        <mo>A</mo>
        <mn>k-1</mn>
    </msup>
    <mi>=</mi>
    <msubsup>
        <mo>a</mo>
        <mn>ij</mn>
        <mn>k-1</mn>
    </msubsup>
</math> 
</h3>

Assim, <math><msubsup><mo>a</mo><mn>ij</mn><mn>k-1</mn></msubsup></math> é a quantidade de caminhos de tamanho k-1 entre os vértices v<sub>i</sub> e v<sub>j</sub>. Logo:

<h3>
<math xmlns='http://www.w3.org/1998/Math/MathML' display='block'>
    <msup>
        <mo>A</mo>
        <mn>k</mn>
    </msup>
    <mi>=</mi>
    <msubsup>
        <mo>a</mo>
        <mn>ij</mn>
        <mn>k</mn>
    </msubsup>
</math> 
</h3>

Nesse caso, sendo A<sup>k</sup> = A<sup>k-1</sup>, temos que <math><msubsup><mo>a</mo><mn>ij</mn><mn>(k)</mn></msubsup></math> é adquirido ao mutiplicarmos os valores da linha i de A<sup>k-1</sup> pelos respectivos valores da coluna j de A e, em seguida, soma-se os valores finais obtidos. Segue abaixo:

<math xmlns='http://www.w3.org/1998/Math/MathML' display='block'>
    <munderover>
        <mo>&sum;</mo>
        <mrow>
            <mi>p</mi>
            <mo>=</mo>
            <mn>1</mn>
        </mrow>
        <mi>n</mi>
    </munderover>
    <msubsup>
        <mo>a</mo>
        <mn>ip</mn>
        <mn>(k-1)</mn>
    </msubsup>
    <msub>
        <mo>a</mo>
        <mn>ij</mo>
</math>

