using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Discord_Bot
{
    class custClass
    {
        //convert between bases
        public static char[] digits = {    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                                    'U', 'V', 'W', 'X', 'Y', 'Z'};
        public static string changeBase(int num, int outnum, int innum = 10)
        {
            //initialize variables
            string output = "";
            bool isneg = false;

            //check some test cases (for robustness purposes)
            if(num == 0) //check to see if number is 0
                return "0";
            if(outnum == innum) //check to see if base doesnt change
                return num.ToString();
            if(num < 0) //check to see if number is negative
            {
                isneg = true;
                num = Math.Abs(num);
            }

            //ensure everything is in base 10 first
            if(innum != 10)
            {
                //do this later lol
            }

            //actually do the math
            do
            {
                int tempdecim = num % outnum; //grabs the digit
                output = digits[--tempdecim] + output; //turns it into a letter if need be. index is one less.
                num /= outnum; // gets the integer remaining (both values are integers.)
            } while(num >= outnum);

            //modify output
            if(isneg == false) //return value to negative sign
                output = "-" + output;

            return output;
        }

        //grabs an appropriate pun
        public static string[] getPuns(string keyword)
        {
            //initialize variables
            List<String> outs = new List<string>();
            List<String> rawPun = new List<string>();
            List<String> rawKey = new List<string>();

            //grabs all the puns from the document
            string[] raw = File.ReadAllLines(@"..\\Resources\\Jokes\\puns.txt");
            foreach(string line in raw)
            {
                string[] lin = line.Split('|'); //pipe is the delimiter
                rawPun.Add(lin[0]);
                rawKey.Add(lin[1]);
            }

            //turns the arraylists into arrays
            string[] puns = rawPun.ToArray();
            string[] keys = rawKey.ToArray();

            //checks for the keyword and, if present, adds it to the output
            for(int i = 0; i < rawPun.Length; i++)
            {
                if(keys[i].Contains(keyword))
                    outs.Add(puns[i]);
            }

            return outs.ToArray();
        }
    }
}
