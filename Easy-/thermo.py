using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Counting
{
    class Program
    {
        static void Main(string[] args)
        {
            ICounter fib = new FibonacciCounter();
            ICounter primes = new PrimeCounter();

            Console.WriteLine($"Fib (1,20) - {string.Join(", ", fib.GetNumbers(1, 20))}");
            Console.WriteLine($"Primes (0,20) - {string.Join(", ", primes.GetNumbers(1, 20))}");
            Console.WriteLine($"Primes (50,200) - {string.Join(", ", primes.GetNumbers(50, 200))}");
        }
    }

    /// <summary>
    /// Interface for a "counter"
    /// Takes a start and end integer and produces an ordered list of numbers in that range
    /// </summary>
    interface ICounter
    {
        /// <summary>
        /// Get the range of integers for this counter from start (inclusive) to end (exclusive)
        /// </summary>
        /// <param name="start">Start of the range (inclusive)</param>
        /// <param name="end">End of the range (exclusive)</param>
        /// <returns>List of all integers between start and end of this counter</returns>
        List<int> GetNumbers(int start, int end);
    }

    /// <summary>
    /// Prime number generator
    /// </summary>
    public class PrimeCounter : ICounter
    {
        public List<int> GetNumbers(int start, int end)
        {
            if(end - start <= 1){ // empty list since start - end doesn't include a prime number
                return new List<int>();
            }
            var list = new List<int>();
        
            for(int num = start; num <= end; num +=1){
                var temp = num;
                for(int i = 2; i < num; i++){
                    if(num % i == 0){// if num is prime, it should terminate
                    if(i == num){
                        
                    }
                    }
                    if(!list.Contains(temp)){
                    list.Add(num);
                    }
                    
                }
            }
            return list;
        }
    }

    /// <summary>
    /// Fibonacci sequence generator
    /// </summary>
    public class FibonacciCounter : ICounter
    {
        public List<int> GetNumbers(int start, int end)
        {
            return new List<int>();
        }
    }


}
