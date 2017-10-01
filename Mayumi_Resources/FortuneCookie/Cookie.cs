using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Discord_Bot_2
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
            Cookie[] asdf = new Cookie[12];
            return asdf;
        }
    }
}
