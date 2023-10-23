package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity6 extends AppCompatActivity {

    EditText et;
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main6);

        et = findViewById(R.id.et);
        Button btn = findViewById(R.id.btn);
        tv = findViewById(R.id.tv);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });
    }

//    public void myclick(){
//        String a = et.getText().toString();
//        int aa = Integer.parseInt(a);
//        String txt = "";
//
//        txt += aa+"*"+1+"="+(aa*1)+"\n";
//        txt += aa+"*"+2+"="+(aa*2)+"\n";
//        txt += aa+"*"+3+"="+(aa*3)+"\n";
//        txt += aa+"*"+4+"="+(aa*4)+"\n";
//        txt += aa+"*"+5+"="+(aa*5)+"\n";
//        txt += aa+"*"+6+"="+(aa*6)+"\n";
//        txt += aa+"*"+7+"="+(aa*7)+"\n";
//        txt += aa+"*"+8+"="+(aa*8)+"\n";
//        txt += aa+"*"+9+"="+(aa*9)+"\n";
//
//
//        tv.setText(txt);
//    }

    public void myclick() {
        String a = et.getText().toString();
        int aa = Integer.parseInt(a);
        StringBuilder txtBuilder = new StringBuilder();

        for (int i = 1; i <= 9; i++) {
            int result = aa * i;
            txtBuilder.append(aa).append("*").append(i).append("=").append(result).append("\n");
        }

        String txt = txtBuilder.toString();
        tv.setText(txt);
    }

}
