#include<bits/stdc++.h>
using namespace std;
int main()
{
    string out;
    string temp;
    string hu;
    string wi;

    float outlook[100][100];
    float yes,no;
    cout<<"P(YES)"<<endl;
    cin>>yes;
    cout<<"P(NO)"<<endl;
    cin>>no;


    float Sunny_Yes=outlook[1][1]=2/9.0f;
    float Sunny_NO=outlook[1][2]=3/5.0f;
    float Overcast_Yes=outlook[1][3]=4/9.0f;
    float Overcast_No=outlook[1][4]=0.0f;
    float Rain_Yes=outlook[1][5]=3/9.0f;
    float Rain_NO=outlook[1][6]=2/5.0f;


    float Hot_Yes=outlook[2][1]=2/9.0f;
    float HOt_NO=outlook[2][2]=2/5.0f;
    float Mild_Yes=outlook[2][3]=4/9.0f;
    float Mild_No=outlook[2][4]=2/5.0f;
    float Cool_Yes=outlook[2][5]=3/9.0f;
    float Cool_NO=outlook[2][6]=1/5.0f;

    float High_Yes=outlook[3][1]=3/9.0f;
    float High_NO=outlook[3][2]=4/5.0f;
    float Normal_Yes=outlook[3][3]=6/9.0f;
    float Normal_No=outlook[3][4]=1/5.0f;

    float Strong_Yes=outlook[4][1]=3/9.0f;
    float Strong_NO=outlook[4][2]=3/5.0f;
    float Weak_Yes=outlook[4][3]=6/9.0f;
    float Weak_NO=outlook[4][4]=2/5.0f;

    cout<< "Enter the Outlook"<< endl;
    cin>>out;
    if(out=="sunny")
    {
        yes=yes * outlook[1][1];
        no=no *outlook[1][2];

    }
    else if(out=="overcast")
    {
        yes=yes*outlook[1][3];
        no=no *outlook[1][4];
    }
    else if(out=="humidity")
    {
        yes=yes*outlook[1][5];
        no=no *outlook[1][6];
    }

    cout<< "Enter the Temperature"<< endl;
     cin>>temp;
    if(temp=="hot")
    {
        yes=yes*outlook[2][1];
        no=no *outlook[2][2];
    }
    else if(temp=="mild")
    {
        yes=yes*outlook[2][3];
        no=no *outlook[2][4];
    }
    else if(temp=="cool")
    {
        yes=yes*outlook[2][5];
        no=no *outlook[2][6];

    }
   cout<< "Enter the Humidity"<< endl;
    cin>>hu;
    if(hu=="high")
    {
        yes=yes*outlook[3][1];
        no=no *outlook[3][2];

    }
    else if(hu=="normal")
    {
        yes=yes*outlook[3][3];
        no=no *outlook[3][4];
    }
    cout<< "Enter the windluy"<< endl;
     cin>>wi;
    if(wi=="strong")
    {
        yes=yes*outlook[4][1];
        no=no *outlook[4][2];

    }
    else if(wi=="weak")
    {
        yes=yes*outlook[4][3];
        no=no *outlook[4][4];
    }


    cout<<"NB(yes)"<<yes<<endl;
    cout<<"NB(no)"<<no<<endl;

    cout << "Normalization From"<<endl;

    float a=yes/(yes+no);
    float b=no/(yes+no);

    cout<<"NB(yes)"<<a<<endl;
    cout<<"NB(no)"<<b<<endl;



    return 0;
}
