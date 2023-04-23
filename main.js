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
            for(let x = 0; x < returnjson.w; x++)
            {
                for(let y = 0; y < returnjson.h; y++)
                {
                    calculator.setExpression({id: x + "x" + y, latex: returnjson.pixels[x * returnjson.h + y], fillOpacity: 1, color: returnjson.colors[x * returnjson.h + y]});
                }
            }
            console.log("done")
        })
    }, 33.33333333);
}

function once()
{
    fetch("http://127.0.0.1/RenderImage")
        .then((response) => {
            return response.json();
        })
        .then((returnjson) => {
            for(let x = 0; x < returnjson.w; x++)
            {
                for(let y = 0; y < returnjson.h; y++)
                {
                    calculator.setExpression({id: x + "x" + y, latex: returnjson.pixels[x * returnjson.h + y], fillOpacity: 1, color: returnjson.colors[x * returnjson.h + y]});
                }
            }
            console.log("done")
        })
}