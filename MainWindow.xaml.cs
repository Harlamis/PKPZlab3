using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace PKPZlab3
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            char[] input = Input.Text.ToCharArray();
            int rs = 0;
            int ks = 0;
            int ts = 0;
            foreach (char c in input)
            {
                switch (c)
                {
                    case 'r':
                        rs++;
                        break;
                    case 'k':
                        ks++;
                        break;
                    case 't':
                        ts++;
                        break;
                }
            }
            r_counter.Content = rs;
            k_counter.Content = ks;
            t_counter.Content = ts;
        }

        private void Input_GotFocus(object sender, RoutedEventArgs e)
        {
            if (Input.Text == "Random text")
            {
                Input.Clear();
            }
        }

    }
}