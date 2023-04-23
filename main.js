var elt = document.getElementById('calculator');
var calculator = Desmos.GraphingCalculator(elt);
//calculator.setExpression({id: 'graph1', latex: 'y<5 \\left\\{3<x<5\\right\\}\\left\\{3<y<5\\right\\}', fillOpacity: 1});

function RenderImage()
{
    setInterval(() => {
        fetch("http://127.0.0.1/RenderImage")
        .then((response) => {
            return response.json();
        })
        .then((returnjson) => {
            for(let i = 0; i < returnjson.pixelCount; i++)
            {
                calculator.setExpression({id: 'graph1', latex: returnjson.pixels[i], fillOpacity: 1});
                console.log()
            }
        })
    }, 33.33333333);
}