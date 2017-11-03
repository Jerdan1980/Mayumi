using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Mayumi_Resources
{
    class Cookie
    {
        public string Fortune;
        public string Numbers;
        public bool Learn;
        public string Chinese;
        public string English;

        public Cookie(string Fortune, String Numbers, bool Learn, String Chinese, String English)
        {
            this.Fortune = Fortune;
            this.Numbers = Numbers;
            this.Learn = Learn;
            this.Chinese = Chinese;
            this.English = English;
        }

        private string getFortune()
        {
            string ret = "";
            return ret;
        }

        public static Cookie[] createObject()
        {
            string path = @"Fortune_Cookies.txt";
            int len = File.ReadAllLines(path).Length;
            Cookie[] asdf = new Cookie[len];
            for(int i = 0; i < len; i++)
            {
                string inp = File.ReadAllLines(path)[i];
                string[] tokens = inp.Split('\"');
            }
            return asdf;
        }
    }
}
