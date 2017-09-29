using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Discord_Bot_2
{
    class Cookie
    {
        public String Fortune;
        public String Numbers;
        public bool Learn;
        public String Chinese;
        public String English;

        public Cookie(string Fortune, String Numbers, bool Learn, String Chinese, String English)
        {
            this.Fortune = Fortune;
            this.Numbers = Numbers;
            this.Learn = Learn;
            this.Chinese = Chinese;
            this.English = English;
        }
    }
}
