using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Discord_Bot
{
    //meant to make the cookie text file usable
    class Cookie
    {
        //the five variables stored in the text file
        public string Fortune; //the fortune itself
        public string Numbers; //the six lucky numbers
        public bool Learn; //if there is a translation
        public string Chinese; //the chinese word
        public string English; //the english meaning of the chinese word

        //converts the string into an array of Cookie objects
        public static Cookie[] fileToArray()
        {
            //initialize variable
            List<Cookie> cook = new List<Cookie>();
            //each line is a single fortune cookie
            String[] inputs = File.ReadAllLines(@"..\\Discord_Bot_2\\Resources\\textSpeech\\fortunes.txt");
            foreach(String raw in inputs){
                cook.Add(new Cookie(raw)); //turns the string into an actual cookie object
            }
            return cook.ToArray();
        }

        //cookie constructor
        public Cookie(string raw)
        {
            createFortune(raw);
        }

        //grabs the information from the string and sticks them into the variables
        private void createFortune(string raw)
        {
            string[] inputs = raw.Split("|"); //pipe is the delimiter
            Fortune = inputs[0];
            Numbers = inputs[1];
            Learn = bool.Parse(inputs[2]);
            if(Learn == true)
            {
                Chinese = inputs[3];
                English = inputs[4];
            }else if (Learn == false)
            {
                Chinese = null;
                English = null;
            }
        }
    }
}
