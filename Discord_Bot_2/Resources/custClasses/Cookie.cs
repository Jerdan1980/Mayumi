using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Discord_Bot
{
    class Cookie
    {
        public string Fortune;
        public string Numbers;
        public bool Learn;
        public string Chinese;
        public string English;

        public static Cookie[] fileToArray()
        {
            List<Cookie> cook = new List<Cookie>();
            String[] inputs = File.ReadAllLines(@"..\\Discord_Bot_2\\Resources\\textSpeech\\fortunes.txt");
            foreach(String raw in inputs){
                cook.Add(new Cookie(raw));
            }
            return cook.ToArray();
        }

        public Cookie(string raw)
        {
            createFortune(raw);
        }

        private void createFortune(string raw)
        {
            string[] inputs = raw.Split("|");
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
