var Stopwatch = require("typescript-dotnet-umd/System/Diagnostics/Stopwatch");

console.log("Elapsed Time:",Stopwatch.default.measure(()=>{
    let n = 0;
    for (let j = 0; j < 10; j++)
    {
        for (let i = 0; i < 1000000000; i++)
        {
            n += i;
        }
    }
}).total.seconds);